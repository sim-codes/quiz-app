from .test_setup import TestCourseSetup

class TestCourseViews(TestCourseSetup):
    def test_course_list(self):
        response = self.client.get(self.course_url)
        self.assertEqual(response.status_code, 200)

    def test_course_detail(self):
        response = self.client.get(self.course_url + f'{self.course.id}/')
        self.assertEqual(response.status_code, 200)

    def test_course_create(self):
        response = self.client.post(self.course_url, {
            'name': 'JavaScript',
            'tutor': self.user.id,
            'description': 'This is a course about JavaScript'
        })
        self.assertEqual(response.status_code, 201)

    # def test_course_update(self):
    #     response = self.client.put(self.course_url + f'{self.course.id}/', {
    #         'name': 'Django',
    #         'tutor': self.user.id,
    #         'description': 'This is a course about Django'
    #     })
    #     self.assertEqual(response.status_code, 200)

    # def test_course_delete(self):
    #     response = self.client.delete(self.course_url + f'{self.course.id}/')
    #     self.assertEqual(response.status_code, 204)