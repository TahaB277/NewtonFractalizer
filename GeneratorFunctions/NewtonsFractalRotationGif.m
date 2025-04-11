function NewtonsFractalRotationGif(f, d, n, fileName)
% -----------------------------------------------------
%     Function to create Newton's Fractal GIF
%     Rotation Factor goes from 1 to 47
% -----------------------------------------------------

syms x
fPrime = diff(f, x);
f = sym2poly(f);
fPrime = sym2poly(fPrime);
X=meshgrid(linspace(-2, 2, d));
r = roots(f);
for rotationFactor=1:47
    Z=X+1i*X';
    a=exp(1i*pi*2/47*(rotationFactor - 1));
    %Newton's Method
    for i=1:n
        Z = Z- a*polyval(f, Z) ./ polyval(fPrime, Z);
    end
    
    R = FindClosestRoot(r, Z);
    
    imagesc(X(1,:),X(1,:),R);
    hold on
    plot(r, LineStyle="none", Marker="pentagram", ...
        MarkerFaceColor="black", MarkerSize=10)
    hold off
    axis off
    exportgraphics(gcf, fileName, 'append', true, ...
        'BackgroundColor', [0 0 0], Resolution=600)
end