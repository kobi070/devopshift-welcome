// vars/myLibrary.groovy

def buildApp() {
    echo "Now building the application..."
    echo "buildApp function is called from myLibrary.groovy"
    // Mock build logic here
}

def deployApp(String branchName) {
    echo "Now deploying the application on branch: ${branchName}..."
    echo "deployApp function is called from myLibrary.groovy"
    // Mock deploy logic here
}

def cleanup() {
    echo "Cleaning up after build and deployment..."
    echo "Cleanup function is called from myLibrary.groovy"
    
    // Mock cleanup logic here
}

def whichBranch(String branchName) {
    echo "Checking out branch: ${branchName}..."
    echo "whichBranch function is called from myLibrary.groovy"
    // Mock branch checking logic here
}

def getVersion() {
    echo "Getting the version number..."
    echo "getVersion function is called from myLibrary.groovy"
    // Mock version retrieval logic here
}

def testApp(){
    echo "Running tests..."
    echo "testApp function is called from myLibrary.groovy"
    // Mock test running logic here
}
