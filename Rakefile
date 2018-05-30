require 'html-proofer'


task :default do
  puts "Running CI tasks..."
  # Runs the jekyll build command for production
  # TravisCI will now have a site directory with our
  # statically generated files.
  sh("JEKYLL_ENV=production bundle exec jekyll build")
  options = { :assume_extension => true,
    # :http_status_ignore => [301, 302],
    # :cache => { :timeframe => '2w' },
    :typhoeus => {
    :ssl_verifypeer => false,
    :ssl_verifyhost => 0 },
    :url_ignore => ['http://diss.herokuapp.com']
  }
  HTMLProofer.check_directory("./_site", options).run
  puts "Jekyll successfully built"
end