netsh interface ip set address "本地连接" static 192.168.1.100 255.255.255.0 192.168.1.1

netsh interface ip set dns "本地连接" static 114.114.114.114 primary

netsh interface ip add dns "本地连接" 8.8.8.8
netsh interface ip add dns "本地连接" 8.8.1.2
netsh interface ip add dns "本地连接" 8.8.3.4
netsh interface ip add dns "本地连接" 8.8.5.6
netsh interface ip add dns "本地连接" 8.8.6.7
