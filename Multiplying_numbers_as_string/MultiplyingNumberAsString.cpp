#include <iostream>
#include <string>

using namespace std;

string multiply(string a, string b)
{
    cout << a << '\t' << b << endl;
    string a_1, b_1;
    bool flag = false;
    for (auto i = a.begin(); i != a.end(); ++i)
    {
        if (!flag && '0' == (*i))
        {
            continue;
        }
        else
        {
            flag = true;
        }
        a_1 += *i;
    }
    flag = false;
    for (auto i = b.begin(); i != b.end(); ++i)
    {
        if (!flag && '0' == (*i))
        {
            continue;
        }
        else
        {
            flag = true;
        }
        b_1 += *i;
    }
    if (a_1.length() == 0 || b_1.length() == 0) {return "0";}
    // int nSmaller = (a_1.length() > b_1.length() ? b_1.length() : a_1.length());
    // string  * pieces = new string[nSmaller];
    string &sSmall = (a_1.length() > b_1.length() ? b_1 : a_1);
    string &sBig = (a_1.length() <= b_1.length() ? b_1 : a_1);
    string *pieces = new string[sSmall.length()];
    int sLen = sSmall.length() - 1;
    for (int i = sLen; i >= 0; --i)
    {
        string sTemp;
        int carry(0);
        for (int j = 0; j < sLen - i; ++j)
        {
            sTemp += '0';
        }
        for (int j = sBig.length() - 1; j >= 0; --j)
        {
            int nTemp = (sSmall[i] - '0') * (sBig[j] - '0') + carry;
            sTemp += nTemp % 10 + '0';
            carry = nTemp / 10;
        }
        if (0 != carry) {sTemp += carry + '0';}
        // cout << sTemp << endl;
        pieces[sLen - i] = (sTemp);
    }
    for (int i = 0; i <= sLen; ++i)
    {
        cout << pieces[i] << endl;
    }
    string front = pieces[0];
    for (int i = 1; i <= sLen; ++i)
    {
        string sTemp = pieces[i];
        string sum;
        int carry(0);
        auto m = front.begin(), n = sTemp.begin();
        for (; m != front.end() && n != sTemp.end(); ++m, ++n)
        {
            int nTemp = ((*m) - '0') + ((*n) - '0') + carry;
            sum += '0' + nTemp % 10;
            carry = nTemp / 10;
        }
        auto k = (m == front.end() ? n : m);
        auto h = (m == front.end() ? sTemp.end() : front.end());
        for (; k != h; ++k)
        {
            int nTemp = ((*k) - '0') + carry;
            sum += '0' + nTemp % 10;
            carry = nTemp / 10;
        }
        if (0 != carry) {sum += carry + '0';}
        while (sum.back() == '0')   {sum.pop_back();}
        front = sum;
    }
    cout << "front: " << front << endl;
    string res;
    for (int i = front.length()-1; i >= 0; --i)
    {
        res += front[i];
    }
    return res;
}