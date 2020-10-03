clear all
close all
fileID = fopen('new.txt','r');
formatSpec = '%f';
new_flows = fscanf(fileID,formatSpec);
temp = new_flows;
indices = find(temp>10);
temp(indices) = [];
m = mean(temp);
for i = 1:length(new_flows)
   if(new_flows(i) > 10)
       new_flows(i) = m;
   end
end
fileID = fopen('existed.txt','r');
existed_flows = fscanf(fileID,formatSpec);
nbins = 100;
h1 = histfit(new_flows,nbins)
hold on
h2 = histfit(existed_flows,nbins)
grid on;
legend('Histogram of RTT for New Flows','Histogram of RTT for Existed Flows')