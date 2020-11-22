using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using bare_minimum.Data;
using bare_minimum.Dtos.School;
using bare_minimum.Dtos.Students;
using bare_minimum.Models;
using bare_minimum.Services.SchoolService;
using bare_minimum.Services.StudentService;
using Microsoft.AspNet.OData;
using Microsoft.AspNet.OData.Query;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Logging;

namespace bare_minimum.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class StudentController : ControllerBase
    {
        private readonly IStudentService StudentService; 
        private readonly ILogger<StudentController> _logger;

        private readonly DataContext _context;

        public StudentController(IStudentService StudentService, ILogger<StudentController> logger, DataContext context)
        {
            this.StudentService = StudentService;
            _logger = logger;
            _context = context;
        }

        [HttpPost]
        public async Task<IActionResult> AddStudent(AddStudentDto addStudent)
        {
            var obj = await this.StudentService.AddStudent(addStudent);
            return Ok(obj);
        }

        // [HttpGet]
        // [EnableQuery]
        // public List<Student> Get()
        // {
        //     var obj = this.StudentService.Get(1);
        //     return obj;
        // }
        [HttpGet]
        public IActionResult Get(ODataQueryOptions<Student> queryOptions)
        {
            var querySettings = new ODataQuerySettings()
            {
                // Workaround for: https://github.com/aspnet/EntityFrameworkCore/issues/10721
                HandleNullPropagation = HandleNullPropagationOption.False
            };

            var query = queryOptions.ApplyTo(_context.Set<Student>(), querySettings);
            return Ok(query);
        }

        
    }
}