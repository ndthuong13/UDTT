#include <bits/stdc++.h>

using namespace std;

struct lohoa
{
    char loaihoa[50];
    int soluong;
    char mausac[50];
    lohoa(char loaihoa[], int soluong, char mausac[])
    {
        strcpy(this->loaihoa,loaihoa);
        this->soluong = soluong;
        strcpy(this->mausac,mausac);
    }
    lohoa()
    {
        strcpy(this->loaihoa,"");
        this->soluong = 0;
        strcpy(this->mausac,"");
    }
};

int Tong(lohoa *b,int n,int k)
{
    if(k==n-1)
    {
        return b[k].soluong;
    }
    else
    {
        return Tong(b,n,k+1) + b[k].soluong;
    }
}

int Tonghoa(lohoa *b, int l, int r, char mauhoa[])
{
    if(l==r)
    {
        if(strcmp(b[l].mausac,mauhoa)==0)
        {
            return b[l].soluong;
        }
        else
        {
            return 0;
        }
    }
    else
    {
        int mid = (l+r)/2;
        int tmp1 = Tonghoa(b,l,mid,mauhoa);
        int tmp2 =  Tonghoa(b,mid+1,r,mauhoa);
        return  tmp1+ tmp2;
    }
}

void show(lohoa *b, int a[], int k )
{
    for(int i=1; i<=k; i++)
    {
        //cout<<b[a[i]-1].loaihoa<<"-"<<b[a[i]-1].mausac;
                cout<<a[i];

        if(i!=k)
            cout<<", ";
    }
    cout<<endl;
}

void khoitao(int *a, int k)
{
    for(int i=1; i<=k; i++)
    {
        a[i] = i;
    }

}



void ppsinhchon(lohoa *b, int *a, int n, int k)
{
    int i;
    khoitao(a,k);
    do
    {
        show(b,a,k);
        //Tim vi tri mà a[i] chưa đạt giới hạn cuối
        i=k;  //Đặt i ở vị trí cuối
        while(i>0 && a[i]==n-k+i)
        {
            i--;
        }

        if (i>0)
        {
            a[i]++;
            i++;
             //Đặt các phần tử sau i thành giới hạn dưới
            while (i <= k) //x[i+1], …, x[k] = can duoi
            {
                a[i] = a[i - 1] + 1;
                i ++;
            }

        }
    }while(i>0);

}

void ppquayluichon(lohoa *b, int *a, int n, int k, int vt){
    if(vt==k+1){
        show(b,a,k);
        return;
    }
    for(int i =a[vt-1]+1;i<=n-k+vt;i++ ){
        a[vt] = i;
        ppquayluichon(b,a,n,k,vt+1);
    }
}






void ppsinhlap(lohoa *b, int *d, int n){
    int i;
    khoitao(d,n);
    do{
        show(b,d,n);
        //Xet tu cuoi ve dau tim vt lien trc doan giam dan
        i = n-1;// xét từ vị trí trc vị trí cuối
        while(i>0 && d[i]>d[i+1]) i--;
        if(i>0){
            int j = n;// tim vi tri ma a[j]>a[i] lan dau tien
            while(d[j]<d[i]) j--;
            swap(d[i],d[j]);
            reverse(d+i+1,d+n+1);
        }
    }while(i>0);
}

void ppquayluilap(lohoa *b, int *d, int n, int vt, bool check[]){
    for(int i=1; i<=n; i++){
        if(!check[i]){
            d[vt] = i;
            if(vt==n){
                show(b,d,n);
            }else{
                check[i] = true;

                ppquayluilap(b,d,n,vt+1,check);

                check[i] = false;
            }

        }
    }
}

int main()
{
    int n = 7;
    lohoa *b = new lohoa[n];
    b[0] = {"Hoa sen",15,"Hong"};
    b[1] = {"Hoa cuc",20,"Vang"};
    b[2] = {"Hoa dao",10,"Hong"};
    b[3] = {"Hoa hue",15,"Trang"};
    b[4] = {"Hoa hong",16,"Do"};
    b[5] = {"Hoa lan",15,"Vang"};
    b[6] = {"Hoa cam tu",25,"Tim"};

    //cau a
    cout<<"Tong so luong hoa: "<<Tong(b,n,0)<<endl;

    //cau b
    char mct[50];
    strcpy(mct,"Hong");
    cout<<"Tong so luong hoa co mau "<<mct<<" la: "<<Tonghoa(b,0,n-1,mct)<<endl;

    //cau c
    int k = 3;
    int a[k+1]={0};
    ppsinhchon(b,a,n,k);
    //ppquayluichon(b,a,n,k,1);

    //cau d
    int d[n+1]={0};
    //ppsinhlap(b,d,n);

    bool check[n+1] = {false};

//    ppquayluilap(b,d,n,1,check);

    delete []b;
    delete []a;
    delete []d;
    delete []check;
    return 0;
}
