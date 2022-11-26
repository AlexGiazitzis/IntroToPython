lines = readlines('test.txt')
f = fopen('test.txt', 'a');
fwrite(f, newline + "Hello from MatLab");
fclose(f);
f = fopen('test.txt'); % mode = read by default
while ~feof(f)
    disp(fgetl(f))
end
disp(ftell(f))
frewind(f); % same as fseek(f, 0, -1)
disp(fgets(f))
fclose(f);
