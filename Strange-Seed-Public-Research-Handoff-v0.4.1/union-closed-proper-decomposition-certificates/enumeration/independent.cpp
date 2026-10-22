#include <bits/stdc++.h>
using namespace std;using Mask=unsigned __int128;
int n,N,U,r,cap;vector<int>G,sup;vector<long long>weights,coef;long long nodes=0,families=0,maxnodes;double limitsec;bool stopped=0,violation=0;vector<int>bad;chrono::steady_clock::time_point start;
ofstream familylog;
Mask allmask;long long minimum_score=LLONG_MAX,minimum_uniform=LLONG_MAX;vector<long long>singlemin,pairmin;
bool bit(Mask m,int t){return m>>t&1;}
int first(Mask m){uint64_t lo=(uint64_t)m;return lo?__builtin_ctzll(lo):64+__builtin_ctzll((uint64_t)(m>>64));}
bool addclose(Mask&pos,vector<int>&H,int t,Mask neg,int&cost,long long&score){
 vector<int> todo={t};
 for(size_t z=0;z<todo.size();z++){
  int a=todo[z];if(bit(pos,a))continue;if(bit(neg,a))return false;
  int extra=2*sup[U^a]+(a==U)-2;for(int h:H)extra+=2*((a|h)==U);
  cost+=extra;if(cost>cap)return false;
  for(int h:H)if(!bit(pos,h|a))todo.push_back(h|a);
  for(int g:G)if(!bit(pos,g|a))todo.push_back(g|a);
  pos|=Mask(1)<<a;H.push_back(a);score+=coef[a];
 }
 return true;
}
void dfs(Mask pos,Mask neg,const vector<int>&H,int cost,long long score){
 if(++nodes>maxnodes){stopped=1;return;}
 if(nodes%1024==0&&chrono::duration<double>(chrono::steady_clock::now()-start).count()>limitsec){stopped=1;return;}
 if(false && score<0){violation=1;bad=H;return;}
 Mask todo=allmask&~(pos|neg);
 if(!todo){families++;familylog<<hex<<setw(16)<<setfill('0')<<(uint64_t)(pos>>64)<<setw(16)<<setfill('0')<<(uint64_t)pos<<"\n";minimum_score=min(minimum_score,score);vector<int>f(n);for(int h:H)for(int i=0;i<n;i++)f[i]+=bool(h>>i&1);
  long long sum=0;for(int i=0;i<n;i++){long long s=2*f[i]-(int)H.size();singlemin[i]=min(singlemin[i],s);sum+=s;}
  minimum_uniform=min(minimum_uniform,sum);int p=0;for(int i=0;i<n;i++)for(int j=i+1;j<n;j++){pairmin[p]=min(pairmin[p],(long long)f[i]+f[j]-(int)H.size());p++;}
  return;
 }
 int t=first(todo);dfs(pos,neg|(Mask(1)<<t),H,cost,score);if(stopped||violation)return;
 vector<int>K=H;Mask pp=pos;int cc=cost;long long ss=score;
 if(addclose(pp,K,t,neg,cc,ss))dfs(pp,neg,K,cc,ss);
}
int main(int argc,char**argv){if(argc<2||argc>3)return 10;familylog.open(argv[1]);cin>>n>>r;if(n<1||n>7)return 2;N=1<<n;U=N-1;G.resize(r);for(int&x:G)cin>>x;weights.resize(n);long long total=0;for(auto&x:weights){cin>>x;total+=x;}cin>>maxnodes>>limitsec;
 for(int a:G)for(int b:G)cap+=(a|b)==U;
 if(argc==3)cap+=stoi(argv[2]);
 sup.assign(N,0);for(int g:G)sup[g]=1;for(int i=0;i<n;i++)for(int t=0;t<N;t++)if(!(t>>i&1))sup[t]+=sup[t|(1<<i)];
 coef.resize(N);for(int t=0;t<N;t++){coef[t]=-total;for(int i=0;i<n;i++)if(t>>i&1)coef[t]+=2*weights[i];}
 singlemin.assign(n,LLONG_MAX);pairmin.assign(n*(n-1)/2,LLONG_MAX);allmask=N==128?~Mask(0):(Mask(1)<<N)-1;
 Mask pos=Mask(1)<<U,neg=0;vector<int>H={U};int rootcost=2*r-1;long long rootscore=total;
 start=chrono::steady_clock::now();
 if(rootcost<=cap){
  for(int t=0;t<U;t++){auto K=H;Mask p=pos;int c=rootcost;long long s=rootscore;if(!addclose(p,K,t,0,c,s))neg|=Mask(1)<<t;}
  dfs(pos,neg,H,rootcost,rootscore);
 }
 cout<<"{\"status\":\""<<(violation?"violation":stopped?"unresolved":"complete")<<"\",\"nodes\":"<<nodes<<",\"families\":"<<families<<",\"elapsed_seconds\":"<<chrono::duration<double>(chrono::steady_clock::now()-start).count()<<",\"minimum_weighted_score\":"<<minimum_score<<",\"minimum_uniform_surplus\":"<<minimum_uniform<<",\"single_coordinate_minima\":[";
 for(int i=0;i<n;i++){if(i)cout<<",";cout<<singlemin[i];}cout<<"],\"pair_minima\":[";for(size_t i=0;i<pairmin.size();i++){if(i)cout<<",";cout<<pairmin[i];}cout<<"],\"witness\":[";for(size_t i=0;i<bad.size();i++){if(i)cout<<",";cout<<bad[i];}cout<<"]}"<<endl;
}
