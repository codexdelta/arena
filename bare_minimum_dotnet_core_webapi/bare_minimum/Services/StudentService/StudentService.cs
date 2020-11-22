using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using bare_minimum.Data;
using bare_minimum.Dtos.Students;
using bare_minimum.Models;


namespace bare_minimum.Services.StudentService
{
    public class StudentService : IStudentService
    {
        private readonly DataContext _context;
        public StudentService(DataContext context)
        {
            _context = context;
        }

        public async Task<List<Student>> AddStudent(AddStudentDto addStudent)
        {   
            School school = _context.SchoolMaster.FirstOrDefault(c => c.Id == addStudent.SchoolId);

            Student student = new Student
            {
                FirstName = addStudent.firstName,
                LastName = addStudent.lastName,
                Age = addStudent.age,
                School = school,
            };

            await _context.StudentMaster.AddAsync(student);
            await _context.SaveChangesAsync();

            List<Student> viva = new List<Student>();
            viva.Add(student);
            return viva;
        }

        public List<Student> Get(int id)
        {
            List<Student> viva = (_context.StudentMaster.Select(c => c).ToList());
            return viva;
        }

    }
}
