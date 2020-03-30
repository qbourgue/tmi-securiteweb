FROM jboss/wildfly

# Add admin user
RUN /opt/jboss/wildfly/bin/add-user.sh admin admin --silent

EXPOSE 8080
EXPOSE 9990

#RUN /opt/jboss/wildfly/bin/standalone.sh

# Configure Keycloak adapter on Wildfly
## Adapter Zip file
ADD keycloak-wildfly-adapter-dist-9.0.2.zip /opt/jboss/
RUN unzip /opt/jboss/keycloak-wildfly-adapter-dist-9.0.2.zip -d /opt/jboss/wildfly/

# Load script to install keycloak adapter
ADD execute.sh /opt/jboss/wildfly/
# Setup keycloak adpater
RUN /opt/jboss/wildfly/execute.sh 

# Launch the server
#RUN /opt/jboss/wildfly/bin/standalone.sh -b 0.0.0.0 &
#RUN ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]
# Wait the server to launch
#RUN sleep 20 
#ADD adapter-install-offline.cli /opt/jboss/
#RUN /opt/jboss/wildfly/bin/jboss-cli.sh -c --file=/opt/jboss/wildfly/bin/adapter-install.cli
#RUN /opt/jboss/wildfly/bin/jboss-cli.sh -c --file=/opt/jboss/wildfly/bin/adapter-elytron-install.cli
#RUN /opt/jboss/wildfly/bin/jboss-cli.sh -c --command=:reload 

CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0", "-bmanagement", "0.0.0.0"]



