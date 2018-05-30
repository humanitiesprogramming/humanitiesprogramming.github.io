require 'html-proofer'

task :test do
  sh "bundle exec jekyll build"
  options = { :assume_extension => true,
    # :http_status_ignore => [301, 302],
    :typhoeus => {
    :ssl_verifypeer => false,
    :ssl_verifyhost => 0 },
    :url_ignore => ['http://diss.herokuapp.com']
  }
  HTMLProofer.check_directory("./_site", options).run
end