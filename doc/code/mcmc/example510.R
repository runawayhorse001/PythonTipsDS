###example 5.10 -- sparrow Poisson regression
yX.sparrow<-dget("http://www.stat.washington.edu/~hoff/Book/Data/data/yX.sparrow")
### sample from the multivariate normal distribution
rmvnorm<-function(n,mu,Sigma)
{
  p<-length(mu)
  res<-matrix(0,nrow=n,ncol=p)
  if( n>0 & p>0 )
  {
    E<-matrix(rnorm(n*p),n,p)
    res<-t(  t(E%*%chol(Sigma)) +c(mu))
  }
  res 
}  

y<- yX.sparrow[,1]; X<- yX.sparrow[,-1]
n<-length(y) ; p<-dim(X)[2]
pmn.beta<-rep(0,p)
psd.beta<-rep(10,p)
var.prop<- var(log(y+1/2))*solve( t(X)%*%X )
beta<-rep(0,p)
S<-10000
BETA<-matrix(0,nrow=S,ncol=p)
ac<-0
set.seed(1)

for(s in 1:S) {
  #propose a new beta
  beta.p<- t(rmvnorm(1, beta, var.prop ))
  lhr<- sum(dpois(y,exp(X%*%beta.p),log=T)) -
    sum(dpois(y,exp(X%*%beta),log=T)) +
    sum(dnorm(beta.p,pmn.beta,psd.beta,log=T)) -
    sum(dnorm(beta,pmn.beta,psd.beta,log=T))
  if( log(runif(1))< lhr ) { beta<-beta.p ; ac<-ac+1 }
  BETA[s,]<-beta
}
  cat(ac/S,"\n")
  #######
  library(coda)
  apply(BETA,2,effectiveSize)
  
  ####
  pdf("sparrow_plot1.pdf",family="Times",height=1.75,width=5)
  par(mar=c(2.75,2.75,.5,.5),mgp=c(1.7,.7,0))
  par(mfrow=c(1,3))
  blabs<-c(expression(beta[1]),expression(beta[2]),expression(beta[3]))
  thin<-c(1,(1:1000)*(S/1000))
  j<-3
  plot(thin,BETA[thin,j],type="l",xlab="iteration",ylab=blabs[j])
  abline(h=mean(BETA[,j]) )
  acf(BETA[,j],ci.col="gray",xlab="lag")
  acf(BETA[thin,j],xlab="lag/10",ci.col="gray")
  dev.off()
  ####
  
    
  
  