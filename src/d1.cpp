#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream f;
    f.open("../i/i1.txt");
    string l;
    vector<string> lines;
    while (f >> l)
    {
        lines.push_back(l);
    }

    int count = 0;
    int prev = stoi(lines[0]);
    for (string& l : lines){
        int cur = stoi(l);
        if (cur > prev) {
            ++count;
        }
        prev = cur;
    }
    cout << "p1 : " << count << endl;

    count = 0;
    int old_sliding = stoi(lines[0]) + stoi(lines[1]) + stoi(lines[2]);
    for (int i = 3; i < lines.size(); ++i) {
        int cur = old_sliding + stoi(lines[i]) - stoi(lines[i - 3]);
        if (cur > old_sliding){
            ++count;
        }
        old_sliding = cur;
    }
    cout << "p2 : " << count << endl;
    
    return 0;
}