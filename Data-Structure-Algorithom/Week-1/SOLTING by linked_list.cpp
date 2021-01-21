#include<stdio.h>
#include<malloc.h>
struct node
{
    int data;
    struct node *link;
};
int main()
{
    struct node *f,*t,*e;
    struct node *t1,*t2,*t3;
    int i,p,c=0;
    for(i=0;i<5;i++)
    {
        t=(struct node* )malloc(sizeof(struct node));
        t->link=NULL;
        scanf("%d",&t->data);
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
    t3=(struct node*)malloc(sizeof(struct node));
    printf("enter data  ");
    scanf("%d",&t3->data);
    printf("enter position  ");
    scanf("%d",&p);
    t=f;
    while(t!=NULL)
    {
        c++;
        if(p==c)
        {
         t3->link=t->link;
         t->link=t3;
        }
        t=t->link;
    }

   /* for(i-0;i<5;i++)
    {
        if(i->data>t3->data && t3->data<(i+1)->data)
        {
            t2=i->link;
            t1->link=t;
            t->link=t2;}
    }*/
    while(f!=NULL)
    {
        printf("%d  ",f->data);
        f=f->link;

    }
}
