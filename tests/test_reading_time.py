
from lib.reading_time import reading_time

def test_calculate_reading_time():
    text = ' Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Suspendisse in est ante in nibh mauris cursus. Donec ac odio tempor orci. Platea dictumst quisque sagittis purus sit amet. Convallis aenean et tortor at. Pellentesque dignissim enim sit amet. Magna fringilla urna porttitor rhoncus dolor purus non enim. In ornare quam viverra orci sagittis eu volutpat odio facilisis. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Amet commodo nulla facilisi nullam vehicula ipsum a. Felis eget nunc lobortis mattis. Molestie nunc non blandit massa enim nec dui nunc mattis. Etiam erat velit scelerisque in dictum non consectetur a erat. Id faucibus nisl tincidunt eget nullam non. Nunc sed blandit libero volutpat sed cras ornare arcu dui. Nulla aliquet enim tortor at auctor urna. At elementum eu facilisis sed odio morbi quis. Et leo duis ut diam quam nulla porttitor massa id. Libero volutpat sed cras ornare arcu dui vivamus. Purus non enim praesent elementum facilisis leo. Auctor elit sed vulputate mi sit amet. Tristique senectus et netus et malesuada fames ac turpis. Orci ac auctor augue mauris augue neque gravida in fermentum. Aliquet eget sit amet tellus cras adipiscing'

    result = reading_time(text)
    assert result == 'Estimated reading time: 1 minute'

    
from lib.reading_time import reading_time

def test_calculate_reading_time():
    text = ' Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Suspendisse in est ante in nibh mauris cursus. Donec ac odio tempor orci. Platea dictumst quisque sagittis purus sit amet. Convallis aenean et tortor at. Pellentesque dignissim enim sit amet. Magna fringilla urna porttitor rhoncus dolor purus non enim. In ornare quam viverra orci sagittis eu volutpat odio facilisis. Euismod nisi porta lorem mollis aliquam ut porttitor leo. Amet commodo nulla facilisi nullam vehicula ipsum a. Felis eget nunc lobortis mattis. Molestie nunc non blandit massa enim nec dui nunc mattis. Etiam erat velit scelerisque in dictum non consectetur a erat. Id faucibus nisl tincidunt eget nullam non. Nunc sed blandit libero volutpat sed cras ornare arcu dui. Nulla aliquet enim tortor at auctor urna. At elementum eu facilisis sed odio morbi quis. Et leo duis ut diam quam nulla porttitor massa id. Libero volutpat sed cras ornare arcu dui vivamus. Purus non enim praesent elementum facilisis leo. Auctor elit sed vulputate mi sit amet. Tristique senectus et netus et malesuada fames ac turpis. Orci ac auctor augue mauris augue neque gravida in fermentum. Aliquet eget sit amet tellus cras adipiscing'

    result = reading_time(text)
    assert result == 'Estimated reading time: 1 minute'

