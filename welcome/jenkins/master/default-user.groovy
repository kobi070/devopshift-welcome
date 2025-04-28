import jenkins.model.*
import hudson.security.*

def env = System.getenv()

// Get the Jenkins instance
def jenkins = Jenkins.get()

// Set the security realm (authentication method)
def securityRealm = new HudsonPrivateSecurityRealm(false)
jenkins.setSecurityRealm(securityRealm)

// Set the authorization strategy (permissions)
def authorizationStrategy = new GlobalMatrixAuthorizationStrategy()
jenkins.setAuthorizationStrategy(authorizationStrategy)

// Create the user account with the provided environment variables
def user = securityRealm.createAccount(env.JENKINS_USER, env.JENKINS_PASS)
user.save()

// Grant the newly created user admin permissions
authorizationStrategy.add(Jenkins.ADMINISTER, env.JENKINS_USER)

// Save the Jenkins instance configuration
jenkins.save()
