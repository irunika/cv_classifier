from core.packages.rake import rake

rob = rake.Rake('../rake/SmartStoplist.txt', 3, 3, 1)

txt = 'java is favourite language'

keywords = rob.run(txt)
print keywords