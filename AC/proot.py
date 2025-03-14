from math import sqrt

class Prim_root:
    def __init__(self, p, g):
        self.p = p
        self.g = g
        
        if not self.is_prime():
            print(f"{p} is not a prime number!!")
        else:
            self.check_primitive_root(self.p, self.g)
            
    
    
    def is_prime(self):
        """Check if a number is prime."""
        if self.p <= 1:
            return False
        if self.p <= 3:
            return True
        if self.p % 2 == 0 or self.p % 3 == 0:
            return False
        i = 5
        while i * i <= self.p:
            if self.p % i == 0 or self.p % (i + 2) == 0:
                return False
            i += 6
        return True
    
    
    def get_prime_factors(n):
        """Return the set of prime factors of n."""
        factors = set()
        
        # Check for factor 2
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        
        # Check for odd factors
        for i in range(3, int(sqrt(n)) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        
        # Add the remaining prime if greater than 2
        if n > 2:
            factors.add(n)
            
        return factors
    
    
    def power_mod(x, y, p):
        """Compute (x^y) % p efficiently."""
        res = 1
        x = x % p
        while y > 0:
            if y % 2 == 1:
                res = (res * x) % p
            y //= 2
            x = (x * x) % p
        return res
    
    
    def find_primitive_roots(prime):
        """Find all primitive roots of a prime number."""
        primitive_roots = []
        
        for base in range(1, prime):
            remainders = set()
            is_primitive = True
            
            for exponent in range(1, prime):
                remainder = pow(base, exponent, prime)
                if remainder in remainders:
                    is_primitive = False
                    break
                remainders.add(remainder)
            
            if is_primitive and len(remainders) == prime - 1:
                primitive_roots.append(base)
                
        return primitive_roots
    
    
    def check_primitive_root(self, prime, candidate, verbose=True):
        """Check if a number is a primitive root of a prime."""
        if not self.is_prime():
            return False, []
        
        primitive_roots = []
        
        for base in range(1, prime):
            remainders = set()
            calculations = []
            
            for exponent in range(1, prime):
                remainder = pow(base, exponent, prime)
                
                if remainder in remainders:
                    break
                elif verbose:
                    calculations.append(f"{base}^{exponent} mod {prime} = {remainder}, ")
                
                remainders.add(remainder)
                
            c = ''.join(calculations)
            
            if len(remainders) == prime - 1:
                primitive_roots.append(base)
                if verbose:
                    print(f"{c.rstrip(", ")} ==> {base} is primitive root of {prime},")
            elif verbose:
                print(f"{c}")
        
        is_primitive = candidate in primitive_roots
        
        if verbose:
            if is_primitive:
                print(f"{candidate} is primitive root: True {primitive_roots}")
            else:
                print(f"{candidate} is NOT primitive root of {prime} - List of Primitive roots: {primitive_roots}")
        
        return is_primitive, primitive_roots