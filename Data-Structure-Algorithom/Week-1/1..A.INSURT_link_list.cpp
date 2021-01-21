#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node *link;
};
int main()
{
     struct node *t,*f,*e;
     struct node *t1,*t2,*t3;

     for(int i=0;i<5;i++)
     {
         t=(struct node*)malloc(sizeof(node));
         //t->data=i+1;
         scanf("%d",&t->data);
         t->link=NULL;
         if(i==0)
         {
             f=t;
         }
         else
         {
            e->link=t;
         }
         e=t;
     }
      t3=(struct node*)malloc(sizeof(node));
      scanf("%d",&t3->data);
      //t3->data=9;
     t1=f->link;
     t2=f->link->link;
     t1->link=t3;
     t3->link=t2;
     while(f!=NULL)
     {
         printf("%d  ",f->data);
         f=f->link;
     }
}
