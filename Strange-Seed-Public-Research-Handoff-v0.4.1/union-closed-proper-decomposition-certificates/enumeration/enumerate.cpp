#include <bits/stdc++.h>
using namespace std;
struct Mask{array<uint64_t,8> a{};void set(int x){a[x/64]|=1ULL<<(x%64);}bool has(int x)const{return a[x/64]>>(x%64)&1;}void merge(const Mask&b,int W){for(int j=0;j<W;j++)a[j]|=b.a[j];}};
int n,N,U,W,cap,hcap,coreq;vector<int> G,sup;vector<Mask> image;vector<long long> coef;vector<int> negatives;vector<char> permitted;
long long nodes=0,visited=0,maxnodes;bool stopped=false;double seconds_limit;chrono::steady_clock::time_point started;
ofstream familylog;
vector<int> answer;long long answer_score=0;int answer_cost=0;
vector<int> members(const Mask&H){vector<int> v;for(int j=0;j<W;j++){uint64_t x=H.a[j];while(x){int b=__builtin_ctzll(x);v.push_back(j*64+b);x&=x-1;}}return v;}
int cost(const vector<int>&H){int q=0;for(int h:H)q+=2*sup[U^h];for(int a:H)for(int b:H)q+=(a|b)==U;return q-2*int(H.size());}
bool canonical(const Mask&K,const Mask&H,int i){int j=i/64,b=i%64;for(int k=0;k<j;k++)if(K.a[k]&~H.a[k])return false;uint64_t low=b?((1ULL<<b)-1):0;return !(K.a[j]&~H.a[j]&low);}
bool dfs(const Mask&H,int next){
 if(++nodes>maxnodes){stopped=true;return false;}
 if(nodes%1024==0&&chrono::duration<double>(chrono::steady_clock::now()-started).count()>seconds_limit){stopped=true;return false;}
 auto hs=members(H);if((int)hs.size()>hcap)return false;
 int c=cost(hs);if(c>cap)return false;visited++;for(int j=W-1;j>=0;j--)familylog<<hex<<setw(16)<<setfill('0')<<H.a[j];familylog<<"\n";
 long long s=0;for(int h:hs)s+=coef[h];
 if(false && s<0){answer=hs;answer_score=s;answer_cost=c;return true;}
 int room=hcap-hs.size();long long bound=s;
 for(int t:negatives)if(t>=next&&!H.has(t)&&permitted[t]){if(room--<=0)break;bound+=coef[t];}
 if(false && bound>=0)return false;
 for(int i=next;i<U;i++){
  if(H.has(i)||!permitted[i])continue;
  Mask K=H;K.merge(image[i],W);for(int h:hs)K.merge(image[h|i],W);
  if(!canonical(K,H,i))continue;
  if(dfs(K,i+1))return true;
  if(stopped)return false;
 }
 return false;
}
int main(int argc,char**argv){if(argc<2||argc>3)return 10;familylog.open(argv[1]);int r;cin>>n>>r;if(n<1||n>9)return 2;N=1<<n;U=N-1;W=(N+63)/64;G.resize(r);for(int&g:G)cin>>g;
 vector<long long> w(n);long long total=0;for(auto&x:w){cin>>x;if(x<0)return 3;total+=x;}if(total<=0||total>1000000000000LL)return 4;cin>>maxnodes>>seconds_limit;
 vector<char> in(N);for(int g:G){if(g<0||g>=N||in[g])return 5;in[g]=1;}if(!in[0]||!in[U])return 6;for(int a:G)for(int b:G)if(!in[a|b])return 7;
 for(int a:G)for(int b:G)cap+=(a|b)==U;coreq=cap;if(argc==3)cap+=stoi(argv[2]);hcap=(cap-2*r+3)/2;
 sup.assign(N,0);for(int g:G)sup[g]=1;for(int i=0;i<n;i++)for(int t=0;t<N;t++)if(!(t>>i&1))sup[t]+=sup[t|(1<<i)];
 image.resize(N);coef.resize(N);permitted.resize(N);
 for(int t=0;t<N;t++){for(int g:G)image[t].set(g|t);long long s=-total;for(int i=0;i<n;i++)if(t>>i&1)s+=2*w[i];coef[t]=s;if(s<0)negatives.push_back(t);}
 sort(negatives.begin(),negatives.end(),[](int a,int b){return coef[a]<coef[b];});
 for(int t=0;t<N;t++)permitted[t]=cost(members(image[t]))<=cap;
 started=chrono::steady_clock::now();Mask root;root.set(U);bool found=dfs(root,0);double elapsed=chrono::duration<double>(chrono::steady_clock::now()-started).count();
 cout<<"{\"status\":\""<<(found?"witness":stopped?"unresolved":"complete_no_violation")<<"\",\"nodes\":"<<nodes<<",\"permissible_nodes\":"<<visited<<",\"qG\":"<<coreq<<",\"cost_cap\":"<<cap<<",\"size_cap\":"<<hcap<<",\"elapsed_seconds\":"<<elapsed<<",\"witness\":[";
 for(size_t j=0;j<answer.size();j++){if(j)cout<<",";cout<<answer[j];}cout<<"],\"witness_score\":"<<answer_score<<",\"witness_cost\":"<<answer_cost<<"}"<<endl;
}
