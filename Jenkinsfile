def branch = '${branch}'

currentBuild.setDisplayName "Build ${version}"

stage 'Create'
node() {
sh "echo Hello Create ${branch}"  
}
stage 'Deploy'
node() {
  sh "echo Hello Deploy"
}
sleep 120
stage 'Test'
node ('') {
  sh "echo Hello Test"
}
