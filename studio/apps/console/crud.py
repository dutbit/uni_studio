from studio.apps.console import console
from flask import render_template,redirect,request,abort,g,url_for,current_app
from studio import models

URL_PATTERN = '/crud/<string:table>'

def get_class(table_name:str):
    if not table_name:
        return None
    target_class = None
    for _class in models.__all__:
        if hasattr(_class,'__tablename__') and _class.__tablename__ == table_name:
            target_class = _class
            break
    return target_class

@console.route(URL_PATTERN,methods=['GET'])
def crud_get(table):
    target_class = get_class(table)
    if not target_class:
        return redirect(url_for('console.console_root'))
    current_app.logger.info(target_class)
    all = target_class.query.all()
    return render_template('common_crud.html',data=all,
        _class=target_class,type=type,
        getattr=getattr,title="crud")

@console.route(URL_PATTERN,methods=['POST'])
def crud_post(table):
    target_class = get_class(table)
    if not target_class:
        return redirect(url_for('console.console_root'))
    
    key = request.values.get('key')
    value = request.values.get('value')
    _id = request.values.get('id')
    if not key or not value:
        abort(500)
    data = target_class.query.filter(getattr(target_class,'id')==_id).first()
    if data:
        setattr(data,key,value)
        models.db.session.commit()
    return redirect(url_for('console.console_root'))