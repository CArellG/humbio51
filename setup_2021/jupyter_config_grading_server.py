# jupyterhub_config.py                                                                                                                                                
c = get_config()
import os
pjoin = os.path.join
runtime_dir = os.path.join('/srv/jupyterhub')

c.JupyterHub.cookie_secret_file = pjoin('/srv/jupyterhub', 'jupyterhub_cookie_secret')
c.JupyterHub.db_url = pjoin('/srv/jupyterhub', 'jupyterhub.sqlite')
c.JupyterHub.ssl_key = '/etc/letsencrypt/live/grading.humbio51.net/privkey.pem'
c.JupyterHub.ssl_cert = '/etc/letsencrypt/live/grading.humbio51.net/fullchain.pem'
c.JupyterHub.port=443
c.Spawner.notebook_dir = '/submissions'
c.Spawner.args=['--NotebookApp.allow_origin=*','--NotebookApp.allow_remote_access=True']
c.Authenticator.whitelist={'annashcherbina','akundaje','asalmeen','soumyakundu'}
c.Authenticator.admin_users={'annashcherbina','akundaje','asalmeen','soumyakundu'}
from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.GitHubOAuthenticator.oauth_callback_url = 'https://grading.humbio51.net/hub/oauth_callback'
c.GitHubOAuthenticator.client_id = 'ba48ae5a7c63f002caff'
c.GitHubOAuthenticator.client_secret = '209e6d648662d11d17f02aa319d9685d15a1c2fe'
