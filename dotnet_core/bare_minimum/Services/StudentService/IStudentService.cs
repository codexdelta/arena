using System.Collections.Generic;
using System.Threading.Tasks;
using bare_minimum.Dtos.Students;
using bare_minimum.Models;

namespace bare_minimum.Services.StudentService
{
    public interface IStudentService
    {
         Task<List<Student>> AddStudent(AddStudentDto addStudent);
         List<Student> Get(int id);
    }
}