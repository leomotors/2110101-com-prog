#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

struct Student
{
    std::string id;
    std::string grade;
};

void readStudentsFromFile(std::ifstream &stream, std::vector<Student> &target)
{
    while (stream.good())
    {
        std::string id, grade;
        stream >> id >> grade;
        target.push_back({id, grade});
    }
}

int main()
{
    std::string f1, f2;
    std::cin >> f1 >> f2;

    std::ifstream file1(f1), file2(f2);

    std::vector<Student> students;

    readStudentsFromFile(file1, students);
    readStudentsFromFile(file2, students);

    std::sort(students.begin(), students.end(), [](Student &s1, Student &s2)
              {
        int64_t s1id = atoll(s1.id.c_str());
        int64_t s2id = atoll(s2.id.c_str());
        int64_t s1f = s1id % 100;
        int64_t s2f = s2id % 100;
        
        if (s1f < s2f) {
            return true;
        }
        else if (s1f > s2f) {
            return false;
        }
        else {
            return s1id < s2id;
        } });

    for (const auto s : students)
    {
        std::cout << s.id << " " << s.grade << "\n";
    }
}
