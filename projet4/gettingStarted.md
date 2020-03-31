# Getting Started _ Projet Sécurité Web: Exercice 2

This document explains how to start Keycloak Docker, WildFly Docker, and a basic application, to experiment Keycloak and Openid Connect.

### Requirement 

- Docker
- Java 8.0 (Java SDK 1.8) or later
- Maven 3.1.1 or later

## Wildfly

#### Build Docker image
This docker image contains WildFly 11. You need to build the docker image to have the keycloak adapter setup.

- Go to WildFly directory
tmi-securiteweb/projet4/WildFly
- Build the docker image:
> docker build -tag wildfly-server .

#### Launch the WildFly docker:
> docker run -p 8080:8080 -p 9990:9990 --network="host" -it wildfly-server

WildFly avalaible on localhost:8080; Admin console on localhost:9990/console

## Keycloak
Docs for this docker image can be seen in: https://www.keycloak.org/getting-started/getting-started-docker

#### Launch the Keycloak docker: 
> docker run -p 8070:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=admin quay.io/keycloak/keycloak:9.0.2

Keycloak will be available on localhost port 8070, with the credentials: admin:admin.

#### Configure Keycloak 
- Go to the Keycloak Web Api
> http://localhost:8070/auth
- Go the Admin console, enter the credentials: admin:admin
- Go to __Import__ section

Import the file *tmi-securiteweb/projet4/keycloak_save/realm-export.json*.

Pick __Skip__ for *if a resource exists*.

#### Configure Keycloak for the App-jsp
The App-jsp use a secret key to communicate with the Keycloak server, you need to generate a new secret, and import it to the config files of the App-jsp.
- Go to *Client__ Section*, click on the *client_id* __app-jsp__
- Go to *Credentials*, Click on __Regenerate Secret__
- Go to *Installation*, Select __Keycloak OIDC JSON__
- Download the keycloak.json file
- Put that keycloak.json into tmi-securiteweb/projet4/keycloak-quickstarts/app-jee-jsp/config/ 


## Service Jaxrs

From Github repertory: https://github.com/keycloak/keycloak-quickstarts

#### Build and Deploy JAX-RS Service
This service is built with *Maven*, it is the base for the App-jsp.
- Go to tmi-securiteweb/projet4/keycloak-quickstarts/service-jee-jaxrs/
- Deploy the service with *Maven*:
> mvn clean wildfly:deploy

- Check the config 

The endpoints for the service are:

public - http://localhost:8080/service/public
secured - http://localhost:8080/service/secured
admin - http://localhost:8080/service/admin

Only public, should be available.

## App jsp

From Github repertory: https://github.com/keycloak/keycloak-quickstarts

See the original tuto : 
https://github.com/keycloak/keycloak-quickstarts/blob/latest/app-jee-jsp/README.md

This is a small web application that interacts with the Keycloak server, to log in users and check their roles.

#### Build and Deploy JAX-RS Service
- Go to tmi-securiteweb/projet4/keycloak-quickstarts/service-jee-jaxrs/
- Deploy the app with *Maven*:
> mvn install wildfly:deploy

- Access the app
> http://localhost:8080/app-jsp

    * Invoke public - Invokes the public endpoint and doesn't require a user to be logged-in.
    * Invoke secured - Invokes the secured endpoint and requires a user with the role user to be logged-in.
    * Invoke admin - Invokes the secured endpoint and requires a user with the role admin to be logged-in.

## Add users in Keycloak
In order to check the functionalities of the web app, you can add new users to Keycloak, with admin or user roles.
- Go the the keycloak administration: http://localhost:8070/
admin:admin
- Go to *Users* section, __Add user__.
- Fill at least the username section, then __Save__.
- Go to the section *Credentials* of this new user, and give him a password.
- Go to the section *Role Mappings* of this new user, and give him roles.

## Shutdown

To shutdown everything, first switch off the app, then the server, then the dockers.

### Undeploy the app and the server
In the directory where it was deployed:
> mvn wildfly:undeploy
### Docker
- List docker
> docker ps -a
- Remove docker
> docker rm docker_id
- Remove all
> docker rm -f $(docker ps -a -q) 
