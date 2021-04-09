clear all
close all
fileID = fopen('secondPing_delay.txt','r');
formatSpec = '%f';
new_flows = fscanf(fileID,formatSpec);
temp = new_flows;
indices = find(temp>14);
temp(indices) = [];
m = mean(temp);
for i = 1:length(new_flows)
   if(new_flows(i) > 14)
       new_flows(i) = m;
   end
end
fileID = fopen('thirdPing_delay.txt','r');
existed_flows = fscanf(fileID,formatSpec);
nbins = 50;
h1 = histfit(new_flows,nbins)
hold on
nbins = 75;
h2 = histfit(existed_flows,nbins)
grid on;
xlabel('{RTT of packets (ms)}','interpreter','latex','FontSize',15)
%% 
clear all
close all

T = 0:0.01:10;
P_e =0.5 * ( qfunc((T-0.85447)/0.900146) + qfunc(-(T-9.52961)/0.696024) );
plot(T,P_e);
hold on
[m,I] = min(P_e);
xline(T(I))
xlabel('{Threshold Value}','interpreter','latex','FontSize',15);
ylabel('{Error Probability}','interpreter','latex','FontSize',15);
