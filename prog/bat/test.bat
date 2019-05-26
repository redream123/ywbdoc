for /f "tokens=4" %%a in ('route print ^|findstr 0.0.0.0.*0.0.0.0') do (  echo %%a)

@(for /f "tokens=3*" %%a in ('netsh interface show interface^|more +2') do @echo,%%b)
