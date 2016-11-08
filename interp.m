function void = interp(x,y,degrees)

    p = polyfit(x,y,degrees);
    x1 = linspace(0, x(length(x)), 100);
    y_int = polyval(p,x1);
    
    plot(x,y, 'o', x1,y_int)