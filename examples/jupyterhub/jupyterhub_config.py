# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.
import os

# Configuration file for Jupyter Hub
c = get_config()

# spawn with Docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# spawn containers from this image
c.DockerSpawner.container_image = os.environ.get(
    'DOCKER_CONTAINER_IMAGE', 'jupyter/singleuser:latest'
)
# use Docker network
network_name = os.environ.get('DOCKER_NETWORK_NAME', 'jupyterhub_default')
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name
c.DockerSpawner.extra_start_kwargs = { 'network_mode': network_name }

# user containers will access hub by container name
c.JupyterHub.hub_ip = 'jupyterhub'
c.JupyterHub.hub_port = 8080

# SSL config
ssl_dir = '/etc/letsencrypt'
c.JupyterHub.port = 443
c.JupyterHub.ssl_key = os.path.join(ssl_dir, 'privkey.pem')
c.JupyterHub.ssl_cert = os.path.join(ssl_dir, 'cert.pem')

# OAuth with GitHub
c.JupyterHub.authenticator_class = 'oauthenticator.GitHubOAuthenticator'
c.GitHubOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# list of allowed and admin users
c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()
c.JupyterHub.admin_access = True
pwd = os.path.dirname(__file__)
with open(os.path.join(pwd, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)
