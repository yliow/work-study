from latextool_basic import *

p = Plot()
D = r"""
class Int
{
public:
        Int (int x = 0)
        : x_(x) {}
        void set(int a) {x_ = a;}
private:
        int x_;
};
int main()
{
    Int a[10];
    for (int i = 0; i < 10; i++)
        a[i].set(i);
...
}
""".strip()
code(p, D)
print(p)


