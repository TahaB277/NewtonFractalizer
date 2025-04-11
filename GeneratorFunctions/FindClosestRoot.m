function r = FindClosestRoot(roots, z)
%-----------------------------------------------------
%     Function that finds the closest root to a point 
%     Inputs :
%         roots
%             roots to test it on
%         z
%             the point (matrix or array)
%     returns:
%         r
%             the closest root to the point
%             1 for roots(1)
%             2 for roots(2)
%             ....
% ------------------------------------------------------

    r = zeros(length(z),length(z));
    
    for i = 1:length(z)
        for j = 1:length(z)
            initial = abs(z(i, j) - roots(1));
            r(i, j) = 1;
            for k = 2:length(roots)
                if  abs(z(i, j) - roots(k)) < initial
                    initial = abs(z(i, j) - roots(k));
                    r(i, j) = k;
                end
            end
        end
    end
end