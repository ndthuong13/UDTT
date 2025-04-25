#include <bits/stdc++.h>

using namespace std;
struct manhinh {
	char hangSX[50];
	double size;
	double price;
	//Constructor loai 3
	manhinh(char hangsx[], double size, double price) {
		strcpy(this->hangSX,hangsx);
		this->size = size;
		this->price = price;
	}
	manhinh() {
		strcpy(this->hangSX,"");
		this->size = 0.0;
		this->price = 0.0;
	}
};
//Thuat toan dung de quy de tinh tong so luong gia cua man hinh
double sumOfPrice(manhinh *d,int n,int i) {
	//Tuong hop suy bien
	if(i == (n - 1)) {
		return d[i].price;
	} else {
		return d[i].price + sumOfPrice(d,n,++i);
	}

}
//Ap dung chien luoc chia de tri de tinh so luong man hinh co kich thuoc lon hon 15.6 inch
int TongSLManHinhCDT(manhinh *d, int l, int r,double size) {
	//Truong hop suy bien
	if(l==r) {
		if(d[l].size>=size)
			return 1;
		else
			return 0;
	} else {
		//Ap dung chien luoc Chia De Tri
		int mid = (l+r)/2;
		int t1 = TongSLManHinhCDT(d,l,mid,size);
		int t2 = TongSLManHinhCDT(d,mid+1,r,size);
		return t1+t2;
	}
}
//Cac ham ho tro cho Ham quay lui
//Ham ho tro tao danh sach ban
void khoiTao(int b[],int n) {
	for(int i = 1; i<= n; i++)
		b[i-1]=i;
}
//Ham ho tro in danh sach
void show(manhinh *d,int b[],int n) {
	for(int i = 0; i<n; i++) {
		cout<<i+1<<"-"<<d[b[i]-1].hangSX<<",";
	}
	cout<<endl;
}


//AP dung chien luoc quay lui de xep n man hinh trong d vao n chiec ban
void xepManHinhql(manhinh *d, int b[], int n, bool check[], int vt,int &count) {
	for(int i=1; i<=n; i++) {
		if(!check[i]) {
			b[vt] = i;
			if(vt==n-1) {
				show(d,b,n);
				count++;
				check[i] = false;
			} else {
				check[i] = true;
				xepManHinhql(d,b,n,check,vt+1,count);
				check[i] = false;
			}
		}
	}
}
int main() {
	//Khoi tao danh sach
	int n = 7;
	manhinh *d = new manhinh();
	d[0]= {"Asus",16.7,1000.5};
	d[1]= {"LG",20.5,1500};
	d[2]= {"HP",14.9,880.5};
	d[3]= {"SamSung",15.5,1000};
	d[4]= {"DELL",13.4,700.9};
	d[5]= {"Sony",15.3,800};
	d[6]= {"Panasonic",30.2,2200};

	//Cau 1 Thuat toan A1
	cout<<"Tong gia ban cua tat cac cac man hinh la: "<<sumOfPrice(d,n,0)<<"!"<<endl;
	cout<<"------------------------------------------------------------------------------------------------- \n";

	//Cau 2 - Thuat toan A2
	double size = 15.6;
	cout<<"Tong so luong man hinh co kich thuoc lon hon 15.6 inch la: "<<TongSLManHinhCDT(d,0,n-1,size)<<endl;


	//Cau 3
	bool check[n]= {false};
	//Bien den so luong cach
	int count =0;
	int vt;
	int b[n];
	khoiTao(b,n);
	cout<<"------------------------------------------------------------------------------------------------- \n";
	xepManHinhql(d,b,n,check,vt,count);
	cout<<"Tong so cach sap xe la: "<<count;

	delete [] d;
	delete [] check;

	return 0;

}
