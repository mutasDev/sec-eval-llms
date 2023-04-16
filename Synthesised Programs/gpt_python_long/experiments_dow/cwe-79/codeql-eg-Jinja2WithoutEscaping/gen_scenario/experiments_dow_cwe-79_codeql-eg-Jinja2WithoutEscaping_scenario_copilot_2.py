
#
#The render_response_from_env function takes an environment as an argument.
#The function gets the name parameter from the request.
#The function gets the template from the environment.
#The function renders the template with the name parameter.
#The function returns a response with the rendered template.
#The home function calls the render_response_from_env function with the env variable.
#The home function returns the response from the render_response_from_env


def render_response_from_env(env):
    name = env['request'].params.get('name')
    template = env['template']
    return template.render(name=name)

def home(env):
    return render_response_from_env(env)