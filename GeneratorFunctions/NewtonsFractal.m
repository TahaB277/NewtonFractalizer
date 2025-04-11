function NewtonsFractal(f, d, n, graphType)
% --------------------------------------------------
%     Function that generates newton's Fractals
%     Inputs:
%         f
%             Function that i want to generate
%             !! before passing this function 
%             write 'syms x' after it declare
%             f(x) = .... (the function)
%         d
%             Dimensions are from -2 to 2
%             d represents nb of points in this inteval
%         n
%             nb of iterations for newton's method
%         graphtype
%             "image" for imagesc
%             "contour" for contourf
% -----------------------------------------------------

syms x
fPrime = diff(f, x);
f = sym2poly(f);
fPrime = sym2poly(fPrime);

X=meshgrid(linspace(-2, 2, d));
Y=meshgrid(linspace(-2, 2, d));
Z=X+1i*Y';

%Newton's Method
for i=1:n
    Z = Z- polyval(f, Z) ./ polyval(fPrime, Z);
end

r = roots(f); 
R = FindClosestRoot(r, Z);

%colors = [YELLOW, BLUE, RED, PURPLE, GREEN];
%c = [1 1 0; 0 0 1; 1 0 0; 0.5 0 0.5; 0 1 0];
%c = [1 1 0; 1 0 0; 0 0 1; 0 1 0; 0.5 0 0.5];

%Image
if graphType == "image"
    imagesc(X(1,:),Y(1,:),R);
elseif graphType == "contour"
    contourf(X(1,:),Y(1,:),R);
end
axis off

%colormap(c);

hold on
plot(r, LineStyle="none", Marker="pentagram", MarkerFaceColor="black", MarkerSize=10)
hold off

%exportgraphics(gca, "Power3Full.png", BackgroundColor="black", Resolution=600)