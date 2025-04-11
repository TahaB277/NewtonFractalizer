function NewtonsFractalCreateGif(f, d, n, fileName)
% -----------------------------------------------------
%     Function to create Newton's Fractal GIF
%     It goes from 1 to n Iterations
% -----------------------------------------------------

syms x
fPrime = diff(f, x);
f = sym2poly(f);
fPrime = sym2poly(fPrime);

X=meshgrid(linspace(-2, 2, d));
Z=X+1i*X';

%Newton's Method
for i=1:n
    Z = Z- polyval(f, Z) ./ polyval(fPrime, Z);
    r = roots(f); 
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