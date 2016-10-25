import pexpect
import re

child = pexpect.spawn('nc vuln2015.icec.tf 9000')
child.expect(".*\nGimme .*")
out = re.search('\d+ .*\\n.*', child.after).group(0)
print(repr(out))
while('Gimme' in out):
    numbers = map(lambda n: int(n), re.findall(r'\b\d+\b', out))
    if 'sum' in out:
        input = sum(numbers)
    elif 'average' in out:
        input = sum(numbers)/float(len(numbers))
    elif 'minimum' in out:
        input = sorted(numbers)[0]
    elif 'maximum' in out:
        input = sorted(numbers)[-1]
    else:
        raise RuntimeError('No case for: ' + out)
    print(input)
    child.sendline(str(input))
    line = child.readline()
    if input == 4:
        print(line)
    child.expect('.*\nGimme .*:')
    out = child.after
    print(out)
# Use shell returned
child.interact()
