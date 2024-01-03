#include <iostream>
#include <vector>

#define INF

using namespace std;

class Dijkstra
{
private:
    /* data */
    vector<double> input_data;
    
    /* private methods */
    


public:
    Dijkstra(const vector<double> &input);
    ~Dijkstra();
};
    
Dijkstra::Dijkstra(const vector<double> &input)
{
    Dijkstra::input_data = input;
}

Dijkstra::~Dijkstra()
{
}