set.seed(1)
s2<-1
t2<-10
mu<-5; n<-5


# rounding the rnorm to 2 decimal places
y<-round(rnorm(n,10,1),2)
# mean of the normal posterior
mu.n<-( mean(y)*n/s2 + mu/t2 )/( n/s2+1/t2)
# variance of the normal posterior
t2.n<-1/(n/s2+1/t2)
# defining the data
y<-c(9.37, 10.18, 9.16, 11.60, 10.33)

theta<-0 ; delta<-2 

rnorm(1,theta,sqrt(delta))

dnorm(y,theta.star,sqrt(s2),log=TRUE)



####metropolis part####
##S = total num of simulations
theta<-0 ; delta<-2 ; S<-10000 ; THETA<-NULL ; set.seed(1)
for(s in 1:S){
  ## simulating our proposal
  #the new value of theta
  #print('theta')
  #print(theta)
  #print('theta.star')
  #print(theta.star)  
  theta.star<-rnorm(1,theta,sqrt(delta))
  ##taking the log of the ratio r
  log.r<-( sum(dnorm(y,theta.star,sqrt(s2),log=TRUE))+ 
             dnorm(theta.star,mu,sqrt(t2),log=TRUE))- 
    ( sum(dnorm(y,theta,sqrt(s2),log=TRUE))+  
        dnorm(theta,mu,sqrt(t2),log=TRUE))
  #print(log.r)
  if(log(runif(1))<log.r) { theta<-theta.star }
  ##updating THETA
  #print(log(runif(1)))
  THETA<-c(THETA,theta)
}
