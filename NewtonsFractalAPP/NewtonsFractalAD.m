function [R,r,X] = NewtonsFractalAD(f, d, n, rotationFactor)

if isempty(rotationFactor)
    rotationFactor = 1;
end

syms x
fPrime = diff(f, x);
f = sym2poly(f);
fPrime = sym2poly(fPrime);

X=meshgrid(linspace(-2, 2, d));
Z=X+1i*X';
a=exp(1i*pi*2/47*(rotationFactor - 1));
%Newton's Method
for i=1:n
    Z = Z- a.*polyval(f, Z) ./ polyval(fPrime, Z);
end

r = roots(f); 
R = FindClosestRoot(r, Z);

