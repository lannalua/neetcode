#include <iostream>
#include <map>
#include <string>
using namespace std;

class Solution
{
public:
    bool isAnagram(string s, string t)
    {
        if (s.size() != t.size())
        {
            return false;
        }
        map<char, int> dict;

        for (char c : s)
        {
            // Se c ainda não estiver no mapa, o C++ o adiciona automaticamente
            // com o valor padrão 0. O operador++ então incrementa este valor.
            dict[c]++;
        }

        for (char c: t)
        {
            if(dict[c]==0){
                return false;
            }
            dict[c]--;
        }
        return true;
    };
};
