# %% Arg
import os
import jinja2
from pprint import pprint as pp

peers_count = os.environ.get("RECEPTOR_NODE_COUNT")
peers_count = int(peers_count) if peers_count else 5

# %% Create peers data

peers_parameters = []

# Create peer parameters without peers relationships
def create_peer_parameters(uid:str, node_port:int = 4444):
    parameters = {}
    parameters['node_name'] = f"node{uid}"
    parameters['node_port'] = node_port
    parameters['node_socket_file_path'] = "/tmp/receptor.sock"
    parameters["peers"] = []
    return parameters

for i in range(peers_count):
    p = create_peer_parameters(i)
    peers_parameters.append(p)
del(i)
del(p)

# Create a mesh network
for parameters in peers_parameters:
    for p_j in peers_parameters:
        if p_j["node_name"] == parameters["node_name"]:
            continue
        parameters["peers"].append({
            "domain": p_j["node_name"],
            "port": p_j["node_port"]
        })
    break
del(parameters)

# %% Jinja template render
def render_receptor_config_file(template_file_name:str, parameters:dict):
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates/")
    template_env = jinja2.Environment(loader=templateLoader)
    template_file = template_file_name
    template = template_env.get_template(template_file)
    config_file = template.render(**parameters)
    return config_file

# %% Write Receptor config files
for parameters in peers_parameters:
    config_file = render_receptor_config_file("receptor-config.yaml", parameters)
    f = open(f"configs/{parameters['node_name']}.yaml", "w")
    f.write(config_file)
    f.close()

# %% Write docker-compose file
config_file = render_receptor_config_file("docker-compose.yaml", {"peers": peers_parameters})
f = open(f"docker-compose.yaml", "w")
f.write(config_file)
f.close()

# %%
