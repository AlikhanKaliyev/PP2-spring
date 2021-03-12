regex_pattern = r"^M{0,3}(C[MD]|D{0,1}C{0,3})(X[CL]|L{0,1}X{0,3})(I[VX]|V{0,1}I{0,3})$"

import re
print(str(bool(re.match(regex_pattern, input()))))