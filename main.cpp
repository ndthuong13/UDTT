#include <bits/stdc++.h>

using namespace std;

struct Hanghoa{
    char tenhang[50];
    float khoiluong;
    float giaban;

    Hanghoa(char tenhang[],float khoiluong,float giaban){
        strcpy(this->tenhang,tenhang);
        this->khoiluong = khoiluong;
        this->giaban=giaban;
    }

    Hanghoa(){
        strcpy(this->tenhang,"");
        this->khoiluong = 0;
        this->giaban=0;
    }
};
 float Tonggiaban(Hanghoa *a, int n, int vt){
    if(vt==n-1){
        return a[vt].giaban;
    }else{
        return a[vt].giaban + Tonggiaban(a,n,vt+1);
    }
 }

 int demhanghoa(Hanghoa *a, int l, int r, float p){
    if(l==r){
        if(a[l].giaban<p)
            return 1;
        else
            return 0;

    }else{
        int mid = (l+r)/2;
        return demhanghoa(a,l,mid,p) + demhanghoa(a,mid+1,r,p);
    }

 }

 void show(Hanghoa *a, int b[], int n){
    for(int i=1; i<=n;i++){
        cout<<a[b[i]-1].tenhang<<" - "<<b[i];
        if(i!=n){
            cout<<", ";
        }
    }
    cout<<endl;
 }

 void Xephanghoaql(Hanghoa *a, int b[], int n, bool check[], int vt){
    for(int i=1; i<=n; i++){
        if(!check[i]){
            b[vt] = i;
            if(vt==n){
                show(a,b,n);
            }else{
                check[i] = true;
                Xephanghoaql(a,b,n,check,vt+1);
                check[i] = false;
            }
        }
    }
 }

 void khoitao(int *d,int n){
    for(int i=1; i<=n;i++){
        d[i]  = i;
    }
 }

void Xephanghoasinh(Hanghoa *a, int b[], int n){
    int i;
    khoitao(b,n);
    do{
        show(a,b,n);

        i = n-1;
        while(i>0&&b[i]>b[i+1]) i--;

        int j=n;
        while(b[j]<b[i]) j--;

        swap(b[i],b[j]);
        reverse(b+i+1,b+n+1);

    }while(i>0);

}

void Chonhanghoasinh(Hanghoa *a, int b[], int n,int k){
    int i;
    khoitao(b,n);
    do{
        show(a,b,k);
        i = k;
        while(i>0&&b[i]==n-k+i) i--;

        if(i>0){
            b[i]++;
            i++;

            while(i<=k){
                b[i] = b[i-1] + 1;
                i++;
            }
        }

    }while(i>0);

}

void Chonhanghoaql(Hanghoa *a, int b[], int n,int k,int vt){
    if(vt==k+1){
        show(a,b,k);
        return;
    }
    for(int i= b[vt-1]+1;i<=n-k+vt;i++){
        b[vt] = i;
        Chonhanghoaql(a,b,n,k,vt+1);
    }
}

int main()
{
    int n = 6;
    Hanghoa *a = new Hanghoa[n];
    a[0] = {"bim bim",0.2,10.000};
    a[1] = {"do choi",0.5,50.000};
    a[2] = {"keo mut",0.1,1.000};
    a[3] = {"qua bong",0.6,100.000};
    a[4] = {"hop banh",0.5,70.000};
    a[5] = {"but",0.2,5.000};

    //cau a
    cout<<"Tong gia ban cua "<<n<<" hang hoa la: "<<Tonggiaban(a,n,0)<<endl;

    //cau b
    float p =  50.000;
    cout<<"So hang hoa co gia tien nho hon "<<p<<" la: "<<demhanghoa(a,0,n-1,p)<<endl;

    //cau c
    bool check[n+1] = {false};
    int d[n+1]={0} ;
    //Xephanghoaql(a,d,n,check,1);
    //Xephanghoasinh(a,d,n);

    //cau d
    int k = 4;
    //Chonhanghoasinh(a,d,n,k);
    Chonhanghoaql(a,d,n,k,1);

    return 0;
}
