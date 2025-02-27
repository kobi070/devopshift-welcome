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