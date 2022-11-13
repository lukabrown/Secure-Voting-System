/*
Project Header
*/

#include <string>

struct vote
{
  std::string name;          // full name
  int DLnum;                 // Drivers License Number
  double timeCast;           // time vote happened
  int votes[10];             // 10 topics to vote from
  std::string party;         // voter party affiliation
  std::string IPaddress;     // network cast from
  std::string MACaddress;    // device cast from
  double verfNum;            // verification number
  int trust = INITIAL_TRUST; // nodes trust in the system
  struct vote *verfNode1;    // pointer to 1st other node verified
  struct vote *verfNode2;    // pointer to 2nd other node verified
};

// function prototypes
struct vote *GenVote();                 // create random "good" vote
struct vote *GenBadVote();              // create bad vote based on random info
struct vote *GenBadVote(struct vote *); // create bad vote based on another vote
void RunSim(int maxVotes, int topics);  // maxVotes = how many votes to sim,
                                       // topics is how many issues each voter can vote on
void PrintReport();
void Init();

// global variables
const int INITIAL_TRUST = 1;

// Parameters: maxVotes topics
int main(int argc, char **argv)
{
  return 0;
}

struct vote *GenVote()
{
  return;
}

struct vote *GenBadVote()
{
  return;
}

struct vote *GenBadVote(struct vote *)
{
  return;
}

void RunSim(int maxVotes, int topics)
{
  return;
}

void PrintReport()
{
  return;
}

void Init()
{
  return;
}
