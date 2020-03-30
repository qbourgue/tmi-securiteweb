# Projet Sécurité Web: Exercice 2

Nous allons suivre l'exemple 4:

Intitulé du sujet:

- Vous pouvez mettre en place une petite application Web dont l'authentification a été mis en oeuvre manuellement avec faiblesse pour la mise en place de règles sur l'authentification.

- contre mesure possible, utilisation d'openid connect, déploiement de [keycloak](https://www.keycloak.org/) pour l'authentification.

## Keycloak and Wildfly configuration

### Requirement 

- Docker
- WildFly 10 running
- Java 8.0 (Java SDK 1.8) or later
- Maven 3.1.1 or later

### Keycloak

- Solution on Docker: 

https://www.keycloak.org/getting-started/getting-started-docker

#### Launch the Keycloak docker: 

docker run -p 8070:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:9.0.2

Keycloak available on localhost port 8070.


### Wildfly
#### Local Install

https://vitux.com/install-and-configure-wildfly-jboss-on-ubuntu/
- Download WildFly
> Version_Number=16.0.0.Final
> wget https://download.jboss.org/wildfly/$Version_Number/wildfly-$Version_Number.tar.gz -P /tmp

- Unzip the WildFly zip 

- Launch WildFly server 
> sh wildfly-10.1.0.Final/bin/standalone.sh

Disponible on localhost:8080; Admin on localhost:9990/console

#### Setup Keycloak adapter for WildFly
- Setup instruction 

https://github.com/keycloak/keycloak-quickstarts/blob/latest/docs/getting-started.md#start-and-configure-the-wildfly-server

- Download the adapter openid for WildFly
> https://www.keycloak.org/downloads.html
In section Client Adapter, OpenId Connect, WildFly.

- Unzip the file inside the installation directory of WildFly.

- Launch the WildFly server (if not done already)
> sh wildfly-10.1.0.Final/bin/standalone.sh

- Configure the adapter
Go to the WILDFLY_DIRECTORY/bin
> ./jboss-cli.sh -c --file=./adapter-install.cli
> ./jboss-cli.sh -c --command:=reload

### Application exemple

From Github repertory: https://github.com/keycloak/keycloak-quickstarts
- Download github repository

#### Setup JAX-RS service 
- Github tuto:
https://github.com/keycloak/keycloak-quickstarts/blob/latest/service-jee-jaxrs/README.md
- Configuration in Keycloak 
Inside tuto
> Move the file keycloak.json to keycloak-quickstarts/service-jee-jaxrs/config/ 

- Build and Deploy JAX-RS Service
> mvn clean wildfly:deploy

- Check the config 
The endpoints for the service are:

public - http://localhost:8080/service/public
secured - http://localhost:8080/service/secured
admin - http://localhost:8080/service/admin

Only public, should be available.

#### Setup App jsp
- Github tuto:
https://github.com/keycloak/keycloak-quickstarts/blob/latest/app-jee-jsp/README.md
- Configuration in Keycloak
Inside tuto
> Move the file keycloak.json to keycloak-quickstarts/app-jee-jsp/config/ 

- Build and Deploy App jee jsp
> mvn install wildfly:deploy

- Access the app
> http://localhost:8080/app-jsp

Invoke public - Invokes the public endpoint and doesn't require a user to be logged-in
Invoke secured - Invokes the secured endpoint and requires a user with the role user to be logged-in
Invoke admin - Invokes the secured endpoint and requires a user with the role admin to be logged-in

#### Add roles in Keycloak
- Go the the keycloak administration: http://localhost:8070/
admin:admin
- Add roles: admin, user
- Add user: + Role mapping admin or user



## Solution sans keycloak

### Simple Docker image for basic authentication

https://github.com/beevelop/docker-nginx-basic-auth
