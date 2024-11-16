clc;
clear;
ini = readtable('./allResAngleRELION.csv');
vec = [0 0 1];

for i = 1:size(ini,1)
    [relionM, relionAng] = tom_eulerconvert_xmipp(ini(i,:).rot, ini(i,:).tilt, ini(i,:).psi);
    vec_rot = tom_pointrotate(vec, relionAng(1), relionAng(2), relionAng(3));
x(i) = vec_rot(1);
y(i) = vec_rot(2);
z(i) = vec_rot(3);
end


numBins = 15;


xEdges = linspace(min(x), max(x), numBins+1);
yEdges = linspace(min(y), max(y), numBins+1);
zEdges = linspace(min(z), max(z), numBins+1);


[~, ~, xBin] = histcounts(x, xEdges);
[~, ~, yBin] = histcounts(y, yEdges);
[~, ~, zBin] = histcounts(z, zEdges);


validIdx = xBin > 0 & yBin > 0 & zBin > 0;
xBin = xBin(validIdx);
yBin = yBin(validIdx);
zBin = zBin(validIdx);
x = x(validIdx);
y = y(validIdx);
z = z(validIdx);


count = zeros(numBins, numBins, numBins);
for i = 1:length(xBin)
    count(xBin(i), yBin(i), zBin(i)) = count(xBin(i), yBin(i), zBin(i)) + 1;
end

pointDensity = zeros(length(x), 1);
for i = 1:length(xBin)
    pointDensity(i) = count(xBin(i), yBin(i), zBin(i));
end
pointDensity = transpose(pointDensity);

results = [x;y;z;pointDensity];
results = transpose(results);
writematrix(results,'rot001vector_coord.txt');


