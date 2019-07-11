## Digital Signature Algorithm outlined in the NIST's Digital Signature Standard (FIPS 186 and revisions)
def new_hash(message):
    digest = 0
    for c in message:
        digest += ord(c)
        digest = digest % 256
    return digest


def mod_inv(n, modulus):
    # Find the multiplicative modular inverse of n
    q = [0, 0]
    r = [modulus, n]
    a = [0, 1]
    index = 2
    while r[len(r) - 1] != 0:
        quotient = r[index - 2] // r[index - 1]
        q.append(quotient)
        remainder = r[index - 2] - q[index] * r[index - 1]
        r.append(remainder)
        # Auxiliary number is the product of quotient and previous aux, plus 2nd previous aux
        aux = a[index - 2] - q[index] * a[index - 1]
        a.append(aux)
        index += 1
    inverse = a[len(a) - 2]
    if inverse < 0:
        inverse += modulus
    return inverse


def sign_message(message):
    # Create a random value k where 1 < k < q (picked arbitrarily in this example)
    k = 48
    # Generate the two-part signature (r,s). If r or s = 0 after a calculation, choose a new k
    r = 0
    s = 0
    while r == 0 or s == 0:
        r = ((g ** k) % p) % q
        if r == 0:
            k += 1
            continue
        s = ((new_hash(message) + x * r) * mod_inv(k, q)) % q
        if s == 0:
            k += 1
            continue
    return [r, s]


def verify(message, signature):
    r = signature[0]
    s = signature[1]
    # Initial check that the message parameters match
    for sig in signature:
        if sig < 0 or sig > q:
            print("Invalid signature")
    # Recalculate the signature r using s and the other public variables
    w = mod_inv(s, q)
    u1 = (new_hash(message) * w) % q
    u2 = (r * w) % q
    v = (((g ** u1) * (y ** u2)) % p) % q
    print(v)
    if v == r:
        print("Signature is valid!")
    else:
        print("Message is compromised!")


# Key lengths L and N are the prime bit sizes. L is bigger and N is less than the hash bit size
# Prime numbers q (length N) and p (length L). p is also picked such that p - 1 is a multiple of q
q = 191
p = 383
# Find a g such that g^q % p == 1. You can use g = h^(p - 1)/q % p for 1 < h < p - 1
# h is chosen arbitrarily. Pick a new h if g = 1.
h = 2
g = int(h ** ((p - 1) / q)) % p
# Choose your private key x where 0 < x < q
x = 29
# Find your public key using g, x, and p
y = (g ** x) % p

# Signing a message
message = "Hello World"
signature = sign_message(message)
print("Signature")
print("r: " + str(signature[0]))
print("s: " + str(signature[1]))

# Verifying a message. Messages 1 and 2 come in, so check which is real!
message1 = "Hello world"
message2 = "Hello World"
print("Verify message 1")
verify(message1, signature)
print("Verify message 2")
verify(message2, signature)
