
from karigor.helper.path_helper import  write_from_template
from karigor.helper.register_route import register_route_in_api_file
from karigor.helper.append_migration import append_model_to_migrations
def modules_create(path: str):

    module_name = path.lower()     
    class_name = path.capitalize()  
    table_name = f"{module_name}s"
    module_names = f"{class_name}s"
    variables = {
        "class_name": class_name,  
        "table_name": table_name,  
        "module_name": module_name,  
        "module_names": module_names,  
    }
    write_from_template('create/modules/templates/models.txt', f'app/modules/{path}/{path}_model.py', context=variables)
    write_from_template('create/modules/templates/repository.txt', f'app/modules/{path}/{path}_repository.py', context=variables)
    write_from_template('create/modules/templates/route.txt', f'app/modules/{path}/{path}_route.py', context=variables)
    write_from_template('create/modules/templates/schemas.txt', f'app/modules/{path}/{path}_schema.py', context=variables)
    write_from_template('create/modules/templates/services.txt', f'app/modules/{path}/{path}_service.py', context=variables)

    register_route_in_api_file(module_name, class_name)
    append_model_to_migrations(module_name, class_name)
